import streamlit as st
import pandas as pd
import datetime

# Initialize session state for data storage
if 'books' not in st.session_state:
    st.session_state.books = pd.DataFrame(columns=[
        'Title', 'Author', 'Genre', 'Year', 'Rating', 
        'Status', 'Start Date', 'End Date', 'Pages', 'Progress'
    ])

# Unique Feature 1: Book recommendations based on genre
def get_recommendations(genre):
    recommendations = {
        'Fantasy': ['The Hobbit', 'Harry Potter Series', 'Game of Thrones'],
        'Sci-Fi': ['Dune', 'Ender\'s Game', 'The Martian'],
        'Mystery': ['Gone Girl', 'The Girl with the Dragon Tattoo', 'Sherlock Holmes'],
        'Romance': ['Pride and Prejudice', 'The Notebook', 'Outlander']
    }
    return recommendations.get(genre, [])

# Unique Feature 2: Mood-based book suggestions
def mood_filter(mood):
    mood_books = {
        'Happy': ['The Alchemist', 'Anne of Green Gables', 'The Little Prince'],
        'Adventurous': ['Jurassic Park', 'Indiana Jones Series', 'The Da Vinci Code'],
        'Thoughtful': ['1984', 'Brave New World', 'Sapiens'],
        'Relaxing': ['The Art of Simple Living', 'The Secret Garden', 'Walden']
    }
    return mood_books.get(mood, [])

# App layout
st.set_page_config(page_title="My Library", layout="wide")
st.title("📚 Personal Library Manager")

# Sidebar with unique features
with st.sidebar:
    st.header("Special Features")
    
    # Book Recommendations
    genre = st.selectbox("Get Recommendations by Genre", 
                        ['Fantasy', 'Sci-Fi', 'Mystery', 'Romance'])
    if st.button("Show Recommendations"):
        rec_books = get_recommendations(genre)
        st.write("Recommended Books:")
        for book in rec_books:
            st.write(f"- {book}")
    
    # Mood Filter
    mood = st.selectbox("Find Books by Mood", 
                       ['Happy', 'Adventurous', 'Thoughtful', 'Relaxing'])
    if st.button("Suggest Books for My Mood"):
        mood_books = mood_filter(mood)
        st.write(f"{mood} Reads:")
        for book in mood_books:
            st.write(f"- {book}")

# Main form for adding books
with st.expander("Add New Book"):
    with st.form("book_form"):
        col1, col2 = st.columns(2)
        with col1:
            title = st.text_input("Title*")
            author = st.text_input("Author*")
            genre = st.selectbox("Genre", ['Fantasy', 'Sci-Fi', 'Mystery', 
                                           'Romance', 'Non-Fiction', 'Biography'])
        with col2:
            year = st.number_input("Year", min_value=1800, max_value=datetime.datetime.now().year)
            rating = st.slider("Rating", 1, 5)
            pages = st.number_input("Number of Pages", min_value=1)
        
        status = st.radio("Reading Status", ['Not Started', 'Reading', 'Completed'])
        submitted = st.form_submit_button("Add Book")
        
        if submitted:
            if title and author:  # Required fields
                new_book = {
                    'Title': title,
                    'Author': author,
                    'Genre': genre,
                    'Year': year,
                    'Rating': rating,
                    'Status': status,
                    'Start Date': datetime.date.today() if status == 'Reading' else None,
                    'End Date': datetime.date.today() if status == 'Completed' else None,
                    'Pages': pages,
                    'Progress': 0
                }
                
                st.session_state.books = pd.concat(
                [st.session_state.books, pd.DataFrame([new_book])],
                 ignore_index=True
                )
                
                
                
                
                
                
                
                
                
                st.success("Book added successfully!")
            else:
                st.error("Please fill in required fields (Title and Author)")

# Display books with editing features
st.header("Your Book Collection")
if not st.session_state.books.empty:
    # Progress update feature
    with st.expander("Update Reading Progress"):
        selected_book = st.selectbox("Select Book", st.session_state.books['Title'])
        progress = st.slider("Progress (%)", 0, 100)
        if st.button("Update Progress"):
            index = st.session_state.books[st.session_state.books['Title'] == selected_book].index[0]
            st.session_state.books.at[index, 'Progress'] = progress
            st.success(f"Progress updated for {selected_book}!")
    
    # Filter options
    col1, col2, col3 = st.columns(3)
    with col1:
        filter_genre = st.multiselect("Filter by Genre", st.session_state.books['Genre'].unique())
    with col2:
        filter_status = st.multiselect("Filter by Status", st.session_state.books['Status'].unique())
    with col3:
        filter_rating = st.slider("Filter by Minimum Rating", 1, 5)

    # Apply filters
    filtered_books = st.session_state.books
    if filter_genre:
        filtered_books = filtered_books[filtered_books['Genre'].isin(filter_genre)]
    if filter_status:
        filtered_books = filtered_books[filtered_books['Status'].isin(filter_status)]
    filtered_books = filtered_books[filtered_books['Rating'] >= filter_rating]

    # Display filtered books
    st.dataframe(filtered_books.style.applymap(lambda x: 'background-color: #e6f3ff' if x == 'Reading' else '', 
                                              subset=['Status']))
    
    # Delete book feature
    with st.expander("Delete Book"):
        book_to_delete = st.selectbox("Select Book to Delete", filtered_books['Title'])
        if st.button("Confirm Delete"):
            st.session_state.books = st.session_state.books[st.session_state.books['Title'] != book_to_delete]
            st.success(f"Deleted {book_to_delete} from your library")
else:
    st.info("No books in your library yet. Add some using the form above!")

# Unique Feature 3: Reading statistics
st.header("📊 Reading Statistics")
if not st.session_state.books.empty:
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Books", len(st.session_state.books))
    with col2:
        completed = len(st.session_state.books[st.session_state.books['Status'] == 'Completed'])
        st.metric("Completed Books", completed)
    with col3:
        avg_pages = int(st.session_state.books['Pages'].mean())
        st.metric("Average Book Length", f"{avg_pages} pages")
    
    # Visualization
    genre_dist = st.session_state.books['Genre'].value_counts()
    st.bar_chart(genre_dist)
else:
    st.info("Add books to see statistics")